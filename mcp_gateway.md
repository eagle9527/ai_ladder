# mcp_gateway
mcp_gateway 

###  ai_ladder  插件地址： 
```
https://plugin.gin-vue-admin.com/#/layout/newPluginInfo?id=106
```
### 插件能力
```
1.支持对接插件 ai_ladder plugin，支持 第三方 mcp 客户端调用。
2.实现mcp server 对第三方API 的调用。
3.实现mcp server 工具动态注册/销毁。
```

###  Streamable HTTP 请求地址

```
  http://127.0.0.1:8081/mcp
```

### go-mcp 用最新版本
```
go get github.com/ThinkInAIXYZ/go-mcp@v0.2.0
```

### 该插件支持一键导入

#### README(有GIF动图演示☺️☺️)
```
https://github.com/eagle9527/ai_ladder/blob/main/mcp_gateway.md
```
### 1.功能展示
### 功能 
![工具列表](https://github.com/eagle9527/ai_ladder/blob/main/tools.png?raw=true)
![工具详情](https://github.com/eagle9527/ai_ladder/blob/main/tool_defail.png?raw=true)
![ai_ladder_mcp_gateway调用](https://github.com/eagle9527/ai_ladder/blob/main/ai_ladder_mcp_gateway.png?raw=true)
![第三方mcp客户端调用](https://github.com/eagle9527/ai_ladder/blob/main/CherryStudio_mcp_gateway.png?raw=true)
![第三方mcp客户端配置](https://github.com/eagle9527/ai_ladder/blob/main/ide_client.png?raw=true)
![Cherry Studio 客户端对话](https://github.com/eagle9527/ai_ladder/blob/main/ide_chart.png?raw=true)


### 2.演示第三方  API 示例
```
package main

import (
	"crypto/md5"
	"encoding/base64"
	"encoding/hex"
	"fmt"
	"math/rand"
	"strings"
	"time"

	"github.com/gin-gonic/gin"
	"net/http"
)

func main() {
	r := gin.Default()

	// MD5 接口
	r.GET("/api/md5", func(c *gin.Context) {
		text := c.Query("input")
		if text == "" {
			c.JSON(http.StatusBadRequest, gin.H{"error": "input 参数是必需的"})
			return
		}
		hash := md5.Sum([]byte(text))
		md5Str := hex.EncodeToString(hash[:])

		//c.String(http.StatusOK, md5Str)

		c.JSON(http.StatusOK, gin.H{
			"input": text,
			"md5":   md5Str,
		})
	})

	// Base64 接口
	r.GET("/api/base64", func(c *gin.Context) {
		text := c.Query("input")
		if text == "" {
			c.JSON(http.StatusBadRequest, gin.H{"error": "input 参数是必需的"})
			return
		}
		encoded := base64.StdEncoding.EncodeToString([]byte(text))
		//c.String(http.StatusOK, encoded)
		c.JSON(http.StatusOK, gin.H{
			"input":  text,
			"base64": encoded,
		})
	})

	// 根据传入的值拼接随机字符串的接口
	r.POST("/api/random", func(c *gin.Context) {
		// 获取传入的参数
		var req struct {
			BaseString string `json:"base_string"  binding:"required"`
			Length     int    `json:"length" binding:"required"`
		}

		if err := c.ShouldBindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "base_string 参数是必需的"})
			return
		}

		// 打印绑定后的 req 数据
		fmt.Println("req", req)

		// 生成 16 位随机数
		var randomStr string
		rand.Seed(time.Now().UnixNano())
		if req.Length != 0 {
			randomStr = generateRandomString(req.Length)
		} else {
			randomStr = generateRandomString(16)
		}

		// 拼接传入的 base_string 和随机生成的字符串
		combinedStr := req.BaseString + randomStr

		c.JSON(http.StatusOK, gin.H{
			"BaseString":  req.BaseString,
			"Length":      req.Length,
			"combinedStr": combinedStr,
		})
		// 返回拼接后的字符串
		//c.String(http.StatusOK, combinedStr)
	})

	r.Run(":8088") // 本地服务启动在 8088 端口
}

// generateRandomString 生成指定长度的随机字符串
func generateRandomString(length int) string {
	const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	var result strings.Builder
	for i := 0; i < length; i++ {
		result.WriteByte(chars[rand.Intn(len(chars))])
	}
	return result.String()
}

```

数据库信息

```

INSERT INTO `mcp_gateway_tool_parameter` (`id`, `created_at`, `updated_at`, `deleted_at`, `name`, `description`, `required`, `param_type`, `data_type`, `tool_id`) VALUES (1, '2025-04-24 13:29:11.000', NULL, NULL, 'input', '需要计算 MD5 的字符串，例如 hello world', 1, 'query', 'string', 1);
INSERT INTO `mcp_gateway_tool_parameter` (`id`, `created_at`, `updated_at`, `deleted_at`, `name`, `description`, `required`, `param_type`, `data_type`, `tool_id`) VALUES (2, '2025-04-24 13:31:23.000', NULL, NULL, 'input', '要进行 Base64 编码的原始字符串', 1, 'query', 'string', 2);
INSERT INTO `mcp_gateway_tool_parameter` (`id`, `created_at`, `updated_at`, `deleted_at`, `name`, `description`, `required`, `param_type`, `data_type`, `tool_id`) VALUES (3, '2025-04-24 13:32:41.000', '2025-04-24 14:44:13.928', NULL, 'length', '生成的随机字符串的长度', 1, 'body', 'int', 3);
INSERT INTO `mcp_gateway_tool_parameter` (`id`, `created_at`, `updated_at`, `deleted_at`, `name`, `description`, `required`, `param_type`, `data_type`, `tool_id`) VALUES (4, '2025-04-24 13:33:24.000', '2025-04-24 16:52:37.047', NULL, 'base_string', '输入字符串', 1, 'body', 'string', 3);



INSERT INTO `mcp_gateway_tools` (`id`, `created_at`, `updated_at`, `deleted_at`, `name`, `description`, `api_url`, `method`, `status`) VALUES (1, '2025-04-24 13:18:39.790', '2025-04-24 13:28:03.565', NULL, 'md5_local', '本地计算字符串的 MD5 值（通过 Gin 接口）', 'http://localhost:8088/api/md5', 'GET', 1);
INSERT INTO `mcp_gateway_tools` (`id`, `created_at`, `updated_at`, `deleted_at`, `name`, `description`, `api_url`, `method`, `status`) VALUES (2, '2025-04-24 13:19:06.102', '2025-04-24 16:48:03.554', NULL, 'base64_local', '将字符串进行 Base64 编码', 'http://localhost:8088/api/base64', 'GET', 1);
INSERT INTO `mcp_gateway_tools` (`id`, `created_at`, `updated_at`, `deleted_at`, `name`, `description`, `api_url`, `method`, `status`) VALUES (3, '2025-04-24 13:19:52.326', '2025-04-24 16:52:37.045', NULL, 'random_local', '生成指定长度的随机字符串', 'http://localhost:8088/api/random', 'POST', 1);
```
