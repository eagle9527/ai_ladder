##  AI 知识库插件 (knowledge)


 插件名称：AI 知识库（knowledge）
 ### 该插件支持一键导入
 ### 该插件支持，插件（ai_ladder) 直接对接知识库索引
 ### 配置文件添加（支持直接对接GPUStack做向量化）
```
knowledge:
    milvus_address: "localhost:19530"              #milvus地址
    username: "root"                               #milvus账号
    password: "xxxxxxxxxxxxxxxxxxxx"   #milvus密码
    embedding_api_url: "http://localhost/v1/embeddings"                              #向量大模型API
    embedding_api_key : "gpustack_xxxxxxxxxxxxxxxxxxxxxxxxxx" #向量大模型API Key
    embedding_model: "nomic-embed-text-v1.5"                                         #向量模型
    dim: 768                                                                         #维度设定(不同的模型维度不一样)

```
### 功能展示
### 功能 
![问答](https://github.com/eagle9527/ai_ladder/blob/main/knowledge_chart.png?raw=true)
![向量检索](https://github.com/eagle9527/ai_ladder/blob/main/search.png?raw=true)
![知识库](https://github.com/eagle9527/ai_ladder/blob/main/knowledge.png?raw=true)


📌 插件核心能力：
### ✅ 1. 知识内容向量化存储
```
支持上传 文本（txt、docx、pptx） 等格式文件；
自动提取文本内容，并通过本地或远程 Embedding 模型（如OpenAI, Nomic, DeepSeek 等）转为向量；
将文本切片并存入 Milvus 向量数据库，实现高效语义检索；
```
### ✅ 2. 多数据库/多集合支持
```
	支持逻辑分库管理（例如按业务线、项目划分）；
	每个数据库下可管理多个集合（collection），支持按需检索；
	支持切换查询范围：当前库 / 全库检索；
```
### ✅ 3. 向量化语义检索接口
```
	提供统一的检索接口（SearchAll / SearchOne）：
	支持传入自然语言问题；
	通过向量相似度匹配相关内容；
	可返回多个高相关知识片段及匹配度（Score）；
	支持设定 TopK、阈值过滤、排序裁剪等。
```
### ✅ 4. AI 推理辅助增强
```
	插件通常作为 AI 推理服务的前置知识增强模块；
	结合大语言模型（如 GPT / DeepSeek），将检索结果拼接成系统提示词，控制 AI 回答范围；
	实现“基于知识库”的高可信度问答。
```

### ✅ 5. 接口开放与可集成性
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
