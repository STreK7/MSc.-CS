const SHA26 = require('crypto-js/sha256');
class Block{
constructor(index , timestapms , data , previousHash = ''){
this.index = index; this.timestapms = timestapms; this.data = data; this.previousHash = previousHash; this.hash = this.calculateHash(); this.nounce = 0;
}
calculateHash(){
return SHA26(this.index + this.previousHash + this.timestapms + JSON.stringify(this.data) + this.nounce).toString();} mineBlock(difficulty){
while(this.hash.substring(0,difficulty) !== Array(difficulty + 1).join("0")){
this.nounce++;
this.hash = this.calculateHash();
}
console.log("Block mined :" + this.hash);
}
}
class Blockchain{ constructor(){
this.chain = [this.createGenesisisBlock()];
this.difficulty = 4;
}
createGenesisisBlock(){
return new Block(0, "09/09/2022", "Genesis Block","0");
}
getLatestBlock(){
return this.chain[this.chain.length - 1]
}
addBlock(newBlock){
newBlock.previousHash = this.getLatestBlock().hash; newBlock.mineBlock(this.difficulty); this.chain.push(newBlock);
}
}
let ZeeCoin = new Blockchain(); console.log("mining block 1..");
ZeeCoin.addBlock(new Block(1,"18/09/2021",{amount : 4})); console.log("mining block 2..");
ZeeCoin.addBlock(new Block(2,"28/09/2021",{amount : 8}));
