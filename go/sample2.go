package main

import (
	"github.com/gin-gonic/gin"
	"github.com/gin-contrib/sessions"
	"net/http"
)

func countup(c *gin.Context) {
	session := sessions.Default(c)
	var count int
	v := session.Get("count")
	if v == nil {
		count = 0
	} else {
		count = v.(int)
		count++
	}
	session.Set("count", count)
	session.Save()
	c.HTML(http.StatusOK, "sample2.html", gin.H{
		"count": count,
	})
}

func countupReset(c *gin.Context) {
	session := sessions.Default(c)
	count := 0
	session.Set("count", count)
	session.Save()
	c.HTML(http.StatusOK, "sample2.html", gin.H{
		"count": count,
	})
}
