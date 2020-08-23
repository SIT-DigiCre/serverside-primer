package main

import (
	"github.com/gin-gonic/gin"
	"github.com/gin-contrib/sessions"
	"github.com/gin-contrib/sessions/cookie"
)

func main() {
	router := gin.Default()

	router.LoadHTMLGlob("templates/*")

	store := cookie.NewStore([]byte("がっこうぐらし！"))
	router.Use(sessions.Sessions("mysession", store))

	router.GET("/", welcome)
	router.GET("/countup", countup)
	router.POST("/countup", countupReset)
	router.GET("/numguess", numguess)
	router.POST("/numguess", numguessPost)

	router.Run(":8000")
}
