package handler

import (
	"github.com/gin-gonic/gin"
)

type Handler struct {
}

func (h *Handler) InitRoutes() *gin.Engine {
	router := gin.New()

	auth := router.Group("/event")
	{
		auth.GET("/", func(c *gin.Context) {
			c.JSON(200, gin.H{
				"message": "Welcome to the event!",
			})
		})
	}
	return router
}
