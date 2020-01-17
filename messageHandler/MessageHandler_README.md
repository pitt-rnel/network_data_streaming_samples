MessageHandler is a lightweight message passing framework that utilizes a
[`rpclib`](http://rpclib.net/)  backend to improve the speed of message passing. To use, build the
messageHandler executable with `make` and run the executable to start a RPC server. When the RPC
server is running, other programs can make calls to the server through RPC clients. This RPC
framework has several benefits:

- It is built on the [boost.asio](https://www.boost.org/doc/libs/1_66_0/doc/html/boost_asio.html) C++
libraries, which utiilizes asynchronous message passing for faster processing.

- RPC libraries are available across languages. While the server for messageHandler is run in C++,
RPC clients can be created in Python using
[`msgpack-rpc`](https://github.com/msgpack-rpc/msgpack-rpc) to integrate messages across modules
that are written in different languages.
