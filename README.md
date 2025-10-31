# Distributed Key-Value Store

## Overview

A minimal distributed key-value (KV) store, built for learning and extensibility. The project demonstrates key distributed systems concepts including consistency models, replication, partitioning, and practical tradeoffs. It is designed as an educational foundation and portfolio reference, tightly aligned with modern systems design interviews and backend architecture practice.

## [TODO] Considerations

- what is the independent variable and how does that affect decision?
  - throughput, consistency, concurrency control, storage (memory vs disk), etc.
- Key questions:
  - What is the actual use case?
  - What are the throughput requirements?
    - What will be the bottleneck? E.g. disk, RAM, NIC, etc
  - What is the scale/volume of data?
  - What are the latency requirements?
  - What is our consistency model?
    - eventually consistent (replication/partitioning)
    - strong (RAFT, consensus)
  - What are the specific semantics that we are supporting?
    - just get/set?
    - delete?
    - update?
    - others, e.g. update 2 values transactionally?
  - what about a secondary index? (sort order, joins)

## Scope

- Just GET/SET?
  - don’t worry about DELETE
  - SET will overwrite an existing key
- For now, placeholder wire protocol can just be:
  - keys and values cannot have spaces
  - messages are operation (GET or SET) <space> key <space> value
- Use UDP over [localhost](http://localhost) to not worry about connections
- Aim to support 2 clients on one machine speaking to same the same server, which simply blocks while servicing each client
- Do it all in memory; worry about persistence later
