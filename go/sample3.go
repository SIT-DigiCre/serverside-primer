package main

import (
	"github.com/gin-gonic/gin"
	"github.com/gin-contrib/sessions"
	"net/http"
	"math/rand"
	"time"
	"strconv"
)

func numguess(c *gin.Context) {
	session := sessions.Default(c)
	v := session.Get("rnum")
	if v == nil {
		rand.Seed(time.Now().UnixNano())
		v = 1 + rand.Intn(100)
		session.Set("rnum", v)
		session.Set("count", 0)
	}
	session.Save()
	c.HTML(http.StatusOK, "sample3.html", gin.H{
		"res": "",
	})
}

func numguessPost(c *gin.Context) {
	session := sessions.Default(c)
	count := session.Get("count")
	if count == nil {
		count = 0
		session.Set("count", count)
	}
	rnum := session.Get("rnum")
	if rnum == nil {
		rand.Seed(time.Now().UnixNano())
		rnum = 1 + rand.Intn(100)
		session.Set("rnum", rnum)
		count = 0
		session.Set("count", count)
	}
	num, err := strconv.ParseInt(c.PostForm("num"), 10, 64)
	res := ""
	if err != nil {
		res = "error"
	} else {
		count = count.(int) + 1
		session.Set("count", count)
		res = strconv.Itoa(count.(int)) + "tries, " + strconv.Itoa(int(num)) + ": "
		if int(num) < rnum.(int) {
			res += "small!"
		} else if int(num) > rnum.(int) {
			res += "big!"
		} else {
			res += "Congratulations!"
			session.Delete("rnum")
			session.Delete("count")
		}
	}
	session.Save()
	c.HTML(http.StatusOK, "sample3.html", gin.H{
		"res": res,
	})
}
