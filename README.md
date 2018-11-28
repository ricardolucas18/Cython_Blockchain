# Creating a Blockchain using Cython

Project done for an assignment for the University.

The objective was to create a Blockchain using Cython.

### Technologies used

* Python
* Cython
* C
* SQLite
* Gnupg

### Algorithm used

* SHA256

### Blockchain

The blockchain is just a list of blocks, each block has: it's own digital signature, the digital signature of the previous block and other attributes like username, surname, course, degree...

To generate the digital signature i used SHA256 algorithm, this algorithm is applied to a String that is the sum of all the attributes.

Because we don't have the digital signature of the previous block when creating ther first block, in the first block that attribute it's "0" and the first block it's called genesis block.

### The project

To run this project:

```
 python Run.py 
```
