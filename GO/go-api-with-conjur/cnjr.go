package main


import (
    "os"
    "fmt"
    "time"
    "github.com/cyberark/conjur-api-go/conjurapi"
)

func main() {
	config, err := conjurapi.LoadConfig()
	authnTokenFile := os.Getenv("CONJUR_AUTHN_TOKEN_FILE")
    conjur, err := conjurapi.NewClientFromTokenFile(config,authnTokenFile)
    if err != nil { panic(err) }
	
    for true {

        secretValue, err := conjur.RetrieveSecret(os.Getenv("CONJUR_SECRET_DB_PASSWORD"))
		if err != nil { panic(err) }
        fmt.Println("The secret value is: ", string(secretValue))

       time.Sleep(5 * time.Second)
    }
}