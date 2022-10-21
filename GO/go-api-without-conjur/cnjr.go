package main


import (
    "os"
    "fmt"
    "time"
)

func main() {
  
    for true {
 
       fmt.Println("The secret value is: ", string(os.Getenv("CONJUR_SECRET_DB_PASSWORD")))
       time.Sleep(5 * time.Second)
    }
}