package main

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

func welcome(c *gin.Context) {
	greetings := "Welcome, anonymous."
	// もしクエリパラメータnameの長さが0以上だった場合
	if (0 < len(c.Query("name"))) {
		greetings = "Hello, " + c.Query("name") + "."
	}
	c.HTML(http.StatusOK, "sample1.html", gin.H{
		"greetings": greetings,
	})
}
