const SHA26 = require('crypto-js/sha256');
class Block{
constructor(index , timestapms , data , previousHash = ''){
this.index = index; this.timestapms = timestapms; this.data = data; this.previousHash = previousHash; this.hash = this.calculateHash();
}
calculateHash(){
return SHA26(this.index + this.previousHash + this.timestapms + JSON.stringify(this.data)).toString();
}
}
class Blockchain{ constructor(){
this.chain = [this.createGenesisisBlock()];
}
createGenesisisBlock(){
return new Block(0, "01/01/2017", "Genesis Block","0");
}
getLatestBlock(){
return this.chain[this.chain.length - 1]
}
addBlock(newBlock){
newBlock.previousHash = this.getLatestBlock().hash; 
newBlock.hash = newBlock.calculateHash(); 
this.chain.push(newBlock);}
ischainValid(){
for(let i = 1; i < this.chain.length; i++){ 
const currentBlock = this.chain[i];
const previousBlock = this.chain[i-1]; 
if(currentBlock.hash !== currentBlock.calculateHash()){ 
return false;
}
if(currentBlock.previousHash !== previousBlock.hash){ 
return false;
}
}
return true;
}
}
let YashCoin = new Blockchain();
YashCoin.addBlock(new Block(1,"08/08/2022",{amount : 4})); 
YashCoin.addBlock(new Block(2,"09/09/2022",{amount : 10})); 
console.log("is Block chain Valid ? " + YashCoin.ischainValid()); 
console.log("Block Chain Created :\n",JSON.stringify(YashCoin, null , 4));
YashCoin.chain[1].data = { amount: 100}; 
console.log("is Block chain Valid ? " + YashCoin.ischainValid());