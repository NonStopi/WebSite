package main

import (
	"html/template"
	"log"
	"net/http"
)

func index(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles(
		"template/index.html",
		"template/header.html",
		"template/linePoster.html",
		"template/footer.html",
	)

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("Error parsing index template:", err)
		return
	}

	err = t.ExecuteTemplate(w, "index", nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("Error executing index template:", err)
	}
}

func contact(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles(
		"template/contact.html",
		"template/header.html",
		"template/footer.html",
	)

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("Error parsing contact template:", err)
		return
	}

	err = t.ExecuteTemplate(w, "contact", nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("Error executing contact template:", err)
	}
}

func event(w http.ResponseWriter, r *http.Request) {
	t, err := template.ParseFiles(
		"template/event.html",
		"template/header.html",
		"template/linePoster.html",
		"template/footer.html",
	)

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("Error parsing event template:", err)
		return
	}

	err = t.ExecuteTemplate(w, "event", nil)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("Error executing event template:", err)
	}
}

func handleRequest() {
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("./static/"))))
	http.HandleFunc("/", index)
	http.HandleFunc("/contact/", contact)
	http.HandleFunc("/event/", event)
	log.Println("Server started at :8181")
	if err := http.ListenAndServe(":8181", nil); err != nil {
		log.Fatal("ListenAndServe:", err)
	}
}

func main() {
	handleRequest()
}
