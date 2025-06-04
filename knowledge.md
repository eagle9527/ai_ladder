##  AI 知识库插件 (knowledge)


 插件名称：AI 知识库（knowledge）
 ### 该插件支持一键导入
 ### 该插件支持，插件（ai_ladder) 直接对接知识库索引
 ### 配置文件添加（支持直接对接GPUStack做向量化）
```
knowledge:
    milvus_address: "localhost:19530"              #milvus地址
    username: "root"                               #milvus账号
    password: "xxxxxxxxxxxxxxxxxxxxxxxxx"   #milvus密码
    embedding_text_api_url: "http://localhost/v1/embeddings"                              #向量大模型API
    embedding_text_api_key : "gpustack_xxxxxxxxxxxxxxxxxxxxxxxxx" #向量大模型API Key
    embedding_model: "nomic-embed-text-v1.5"                     #向量大模型名称
    embedding_image_api_url: "http://localhost:8088/embed"       #图片向量化API
    search_image_api_url: "http://localhost:8088/search"         #文本向量化搜索图片API
    embedding_image_username: "admin"                            #图片向量化账号
    embedding_image_password: "xxxxxxxxxxxxxxxxxxxxxxxxx" #图片向量化密码
    text_dim: 768                                                #文本向量化维度
    image_dim: 512                                               #图片向量化维度

```
### 图片向量化服务dockerfile
```
https://huggingface.co/OFA-Sys/chinese-clip-vit-base-patch16 #图片向量化模型地址

https://github.com/eagle9527/ai_ladder/blob/main/docker/Dockerfile #Dockerfile
https://github.com/eagle9527/ai_ladder/blob/main/docker/main.py    #服务，注意模型自行下载
```

### docker-compose
```
version: '3.5'

services:
  clip-fastapi:
    image: clip-fastapi:latest
    container_name: clip-fastapi
    ports:
      - "8088:8000"
    environment:
      BASIC_AUTH_USERNAME: admin
      BASIC_AUTH_PASSWORD: d7131eeba69adaa0d6487bfddabd4b4b
  etcd:
    container_name: milvus-etcd
    image: quay.io/coreos/etcd:v3.5.18
    environment:
      - ETCD_AUTO_COMPACTION_MODE=revision
      - ETCD_AUTO_COMPACTION_RETENTION=1000
      - ETCD_QUOTA_BACKEND_BYTES=4294967296
      - ETCD_SNAPSHOT_COUNT=50000
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/etcd:/etcd
    command: etcd -advertise-client-urls=http://etcd:2379 -listen-client-urls http://0.0.0.0:2379 --data-dir /etcd
    healthcheck:
      test: ["CMD", "etcdctl", "endpoint", "health"]
      interval: 30s
      timeout: 20s
      retries: 3

  minio:
    container_name: milvus-minio
    image: minio/minio:RELEASE.2023-03-20T20-16-18Z
    environment:
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: minioadmin
    ports:
      - "9000:9000"
      - "9001:9001"
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/minio:/minio_data
    command: minio server /minio_data --console-address ":9001"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3

  standalone:
    container_name: milvus-standalone
    image: milvusdb/milvus:v2.5.11
    command: ["milvus", "run", "standalone"]
    security_opt:
      - seccomp:unconfined
    environment:
      ETCD_ENDPOINTS: etcd:2379
      MINIO_ADDRESS: minio:9000
      MILVUS_ENABLE_AUTH: true
      MILVUS_DEFAULT_USER: root
      MILVUS_DEFAULT_PASSWORD: d7131eeba69adaa0d6487bfddabd4b4b

    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/milvus:/var/lib/milvus
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9091/healthz"]
      interval: 30s
      start_period: 90s
      timeout: 20s
      retries: 3
    ports:
      - "19530:19530"
      - "9091:9091"
    depends_on:
      - "etcd"
      - "minio"

  attu:
    container_name: milvus-attu
    image: zilliz/attu:v2.5
    ports:
      - "8000:3000"
    environment:
      - MILVUS_URL=standalone:19530
      - MILVUS_USERNAME=root
      - MILVUS_PASSWORD=d7131eeba69adaa0d6487bfddabd4b4b
    depends_on:
      - standalone

networks:
  default:
    name: milvus
```

### 功能展示
### 功能 
![图片向量化搜索](https://github.com/eagle9527/ai_ladder/blob/main/image-search.png?raw=true)

![问答](https://github.com/eagle9527/ai_ladder/blob/main/knowledge_chart.png?raw=true)
![向量检索](https://github.com/eagle9527/ai_ladder/blob/main/search.png?raw=true)
![知识库](https://github.com/eagle9527/ai_ladder/blob/main/knowledge.png?raw=true)


 插件核心能力：
###  1. 知识内容向量化存储
```
支持上传 文本（txt、docx、pptx） 文件, 图片文件(jpeg、png、gif、webp、bmp、tiff、x-icon)；
自动提取文本内容，并通过本地或远程 Embedding 模型（如OpenAI, Nomic, DeepSeek 等）转为向量；
将文本切片并存入 Milvus 向量数据库，实现高效语义检索；
```
###  2. 多数据库/多集合支持
```
	支持逻辑分库管理（例如按业务线、项目划分）；
	每个数据库下可管理多个集合（collection），支持按需检索；
	支持切换查询范围：当前库 / 全库检索；
```
### 3. 向量化语义检索接口
```
	提供统一的检索接口（SearchAll / SearchOne）：
	支持传入自然语言问题；
	通过向量相似度匹配相关内容；
	可返回多个高相关知识片段及匹配度（Score）；
	支持设定 TopK、阈值过滤、排序裁剪等。
```
###  4. AI 推理辅助增强
```
	插件通常作为 AI 推理服务的前置知识增强模块；
	结合大语言模型（如 GPT / DeepSeek），将检索结果拼接成系统提示词，控制 AI 回答范围；
	实现“基于知识库”的高可信度问答。
```

###  5. 接口开放与可集成性
```
	提供标准 API 接口（支持 REST / MCP）：
	上传文件、创建知识库、插入数据；
	语义检索接口；
	易于嵌入现有业务流程或前端聊天系统中；
	支持 SSE 流式返回，兼容 OpenAI 格式。
```


| 组件                        | 描述                                               |
| ------------------------- | ------------------------------------------------ |
| **Milvus**                | 高性能向量数据库，用于存储与检索文本向量                             |
| **Embedding 模型**          | 用于将文本转向量（如 nomic-embed-text, OpenAI Embedding 等） |
| **Golang 服务层**            | 负责文件解析、向量构建、Milvus 管理与检索                         |
| **Gin + GVA 框架**          | 实现后台管理与接口服务                                      |
| **前端 Vue + Element Plus** | 实现知识库管理界面与文件上传模块                                 |
