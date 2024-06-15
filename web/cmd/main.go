package main

import (
	"log"
	"website/web"
	"website/web/pkg/handler"
	"website/web/pkg/repository"
	"website/web/pkg/service"

	"github.com/spf13/viper"
)

func main() {
	if err := initConfig(); err != nil {
		log.Fatalf("error initalizing configs: %s", err.Error())
	}

	repos := repository.NewRepository()
	services := service.NewService(repos)
	handlers := handler.NewHandler(services)

	srv := new(web.Server)
	if err := srv.Run(viper.GetString("port")); err != nil {
		log.Fatalf("error run: %s", err.Error())
	}
}

func initConfig() error {
	viper.AddConfigPath("configs")
	viper.SetConfigName("config")
	return viper.ReadInConfig()
}
