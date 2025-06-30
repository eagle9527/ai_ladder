插件地址：🔗   https://plugin.gin-vue-admin.com/details/106

全新升级的 AI 对接插件，全面支持 OpenAI 标准协议，一键连接 GPUStack、DeepSeek、阿里云百炼、智谱、月之暗面等顶级大模型平台，轻松打造强大的智能应用！

✨ 核心亮点
✅ 即插即用：全面兼容 OpenAI 接口标准，无需额外适配
✅ 多平台支持：原生支持 GPUStack、DeepSeek、阿里云百炼、智谱、月之暗面
✅ 强力集成 Dify 智能体：支持 Chatflow、Agent、聊天助手、文本生成等智能模式
✅ 灵活参数输入：支持 input、number、paragraph 类型，满足多样化场景
✅ 🔥 新增功能：支持 Dify 问答知识库图文混排显示，文本与图片完美融合，知识更直观、更生动！

🎯 应用场景
企业 AI 助手构建

个性化智能工作流自动化

智能问答、知识检索、内容生成

🎉 立即体验插件的全新能力，释放你的 AI 创造力，驱动业务智能化升级！

# ai_ladder
ai_ladder plugin

```
这是一个基于 MCP-Go 的 AI 推理与工具执行服务端组件，通过 SSE 向前端实时推送 AI 推理和工具调用的过程，最终输出结果，并持久化历史记录。
```
### MCP  Gateway 插件地址
```
https://plugin.gin-vue-admin.com/details/111 
```
### MCP 流程图
```
+----------------------+
| 用户发起对话请求     |
+----------------------+
           |
           v
+----------------------------+
| 初始化上下文 + 模型信息   |
| ConnectLoop 连接 MCP SSE |
+----------------------------+
           |
           v
+---------------------------+
| 获取工具列表（ListTools）|
+---------------------------+
           |
           v
+----------------------------------------+
|      进入推理循环（直到终止）          |
+----------------------------------------+
           |
           v
+-----------------------------------------------+
| LLM 推理下一个工具（ExtractNextTool）         |
| --> tool 名称 + 参数 JSON                      |
+-----------------------------------------------+
           |
           v
+----------------------------------+
| resolveParameters                |
| 占位符参数替换 {{tool.field}}    |
+----------------------------------+
           |
           v
+-------------------------------+
| TryCallToolWithRetry          |
| 调用 MCP 工具（含重试机制）   |
+-------------------------------+
           |
           v
+-------------------------------+
| parseAndSendToolResult        |
| SSE 推送返回内容到前端        |
+-------------------------------+
           |
           v
+-----------------------------------------+
| 更新 historyLog + outputs（中间结果）   |
+-----------------------------------------+
           |
           v
       [是否继续？]
        /       \
       /否       \是
      v           v
+--------------------------+       <--- 回到 ExtractNextTool
| finalizeWithLLM          |
| LLM 总结最终回答         |
| SSE 分段输出             |
+--------------------------+
           |
           v
+----------------------------+
| 保存历史记录到数据库      |
+----------------------------+
           |
           v
     +------------------+
     | 推理流程结束 ✅   |
     +------------------+
```
###  配置文件新增
```
ai_ladder:
    mcp_gateway: "http://localhost:8888/sse"
```
### 插件能力
```
该插件全面兼容OpenAI接口标准，无缝对接GPUStack、DeepSeek、阿里云百炼、月之暗面、智谱等业界领先的AI计算平台。

   目前已测试的大模型， openai chat地址:
   GPUStack:    http://localhost/v1-openai/chat/completions
   DeepSeek:    https://api.deepseek.com/chat/completions
   阿里云百炼:    https:/[![RhMYX.md.png](https://i.imgs.ovh/2025/06/26/RhMYX.md.png)](https://imgloc.com/image/RhMYX)/dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
   月之暗面:     https://api.moonshot.cn/v1/chat/completions
   智谱:         https://open.bigmodel.cn/api/paas/v4/chat/completions
   chatgpt:      https://api.openai.com/v1/chat/completions
   腾讯元宝:       https://api.hunyuan.cloud.tencent.com/v1/chat/completions
   字节豆包:      https://ark.cn-beijing.volces.com/api/v3/chat/completions
   百川大模型:     https://api.baichuan-ai.com/v1/chat/completions
   本地Ollama模型:  http://localhost:11434/v1/chat/completions

该插件支持对接Dify:
    支持工作流， Chatflow， 聊天助手，Agent，文本生成 智能体，需要传参的工作流仅支持，input，number，paragraph 。
```
  
```
### 该插件支持一键导入

#### README(有GIF动图演示☺️☺️)
```
https://github.com/eagle9527/ai_ladder/blob/main/README.md

### 1.功能展示
### 功能 
[![Chatflow](https://i.imgs.ovh/2025/06/26/RhA3a.png)](https://i.imgs.ovh/2025/06/26/RhA3a.png)

[![文本生成](https://i.imgs.ovh/2025/06/26/RhkQq.png)](https://i.imgs.ovh/2025/06/26/RhkQq.png)

[![工作流](https://i.imgs.ovh/2025/06/26/Rh2u9.png)](https://i.imgs.ovh/2025/06/26/Rh2u9.png)


[![问答](https://i.imgs.ovh/2025/06/26/Rh9yH.png)](https://i.imgs.ovh/2025/06/26/Rh9yH.png)

[![模型创建](https://i.imgs.ovh/2025/06/26/RubgO.png)](https://i.imgs.ovh/2025/06/26/RubgO.png)

[![模型](https://i.imgs.ovh/2025/06/26/RhMYX.png)](https://i.imgs.ovh/2025/06/26/RhMYX.png)

[![历史](https://i.imgs.ovh/2025/06/26/Rh6f4.png)](https://i.imgs.ovh/2025/06/26/Rh6f4.png)

### 动态演示
![演示](https://github.com/eagle9527/ai_ladder/blob/main/yanshi.gif?raw=true)

 
