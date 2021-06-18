package blockchain.learning;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Block {

    public String hash;
    public String previousHash;
    private Book data; //this will be the 'content of the block', in this case a Book instance
    private long timeStamp;

    private int nonce;


    public Block(Book data, String previousHash) {
        this.data = data;
        this.previousHash = previousHash;
        this.timeStamp = new Date().getTime();
        this.hash = calculateHash(); //based on the previous values
    }

    public String calculateHash(){
        String calculatedHash = StringUtil.applySha256(
                previousHash +
                        Long.toString(timeStamp) +
                        Integer.toString(nonce) +
                        data
        );
        return calculatedHash;
    }

    public void mineBlock(int difficulty){
        String target = new String(new char[difficulty]).replace('\0', '0'); //Create a string with difficulty * "0"
        while(!hash.substring( 0, difficulty).equals(target)) {
            nonce ++;
            hash = calculateHash();
        }
        System.out.println("Block Mined!!! : " + hash);
    }



}
