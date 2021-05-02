# Trie Server Details
Here, you will find more details about the Server hosting the Trie data structure.

## FAQ
***Where is the server hosted?***

The server is hosted on AWS Electric Beanstalk at http://trie-slingshot.eba-rmufyux3.us-east-2.elasticbeanstalk.com/

***How does the CLI interact with the server?***

The CLI uses python [requests](https://docs.python-requests.org/en/master/), and interacts with the server's various endpoints with POST requests to perform operations.

The server does support GET requests as well, but it is recommended to use POST requests to avoid unexpected bugs.

## About

Current availiable REST endpoints:
If marked "Needs Info", the endpoint takes in a JSON with the name/value pair `{"data": value}`

BASE_URL: <http://trie-slingshot.eba-rmufyux3.us-east-2.elasticbeanstalk.com/>
**Insert this URL where it says BASE_URL in the** `curl` **commands**

* insert - Inserts a keyword into the trie
    * **Needs Info** - The value can be an list of strings or just a string

    * `curl -d '{"data": ["arg1", "arg2", ...]}' -H "Content-Type: application/json" -X POST BASE_URL/insert`

    * `curl -d '{"data": "arg"}' -H "Content-Type: application/json" -X POST BASE_URL/insert`

* delete - Deletes a keyword from the trie
    * **Needs Info** - The value can be an list of strings or just a string

    * `curl -d '{"data": ["arg1", "arg2", ...]}' -H "Content-Type: application/json" -X POST BASE_URL/delete`

    * `curl -d '{"data": "arg"}' -H "Content-Type: application/json" -X POST BASE_URL/delete`


* dump - Returns a JSON of the root node.
    * `curl -X POST BASE_URL/dump`

* find - Returns True or False depending if the keyword was found in the trie
    * **Needs Info** - The value must be a string

    * `curl -d '{"data": "arg"}' -H "Content-Type: application/json" -X POST BASE_URL/find`

* autocomplete - Returns a list of autocomplete suggestions based on the input prefix
    * **Needs Info** - value must be a string

    * `curl -d '{"data": "arg"}' -H "Content-Type: application/json" -X POST BASE_URL/autocomplete`

## Contributing

Pull requests are always welcome 😃.

## License

[MIT](https://choosealicense.com/licenses/mit/)
