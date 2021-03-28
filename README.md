# Cerebro
> A lightweight blockchain implementation

The real subject matter or "business logic" will come after my initial implementation.

## Running the Master Node 

The master node connects to the database to deliver the node list to the other nodes.
A single node requires the master node url in order to function in the decentralized network and validate the chain.

### To Run:
Be sure all config fields prefixed with `db_` are set.

```bash
./start_master.sh
```

## Running a Mining Node 

The mining node holds the actual implementation of the blockchain 
and connects to the master node to retrieve all other connections
and interact with the network to keep the blockchain validated.

### To Run:
Fill in `master_api_url` in your config/config.json 
and be sure the master node is running at this url.

```bash
./start_node.sh
```
