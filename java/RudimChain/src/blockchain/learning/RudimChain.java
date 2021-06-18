package blockchain.learning;

import java.util.ArrayList;
import com.google.gson.GsonBuilder;
import com.google.gson.internal.bind.util.ISO8601Utils;

//based on https://github.com/CryptoKass/NoobChain-Tutorial-Part-1
public class RudimChain {

    public static ArrayList<Block> blockchain = new ArrayList<Block>();
    public static int difficulty = 4;

    public static void main(String[] args) {

        Book book1 = new Book("Dirk Bracke","Spoor");
        System.out.println(book1);
        blockchain.add(new Block(book1, "0"));
        System.out.println("Trying to Mine block 1... ");
        blockchain.get(0).mineBlock(difficulty);

        Book book2 = new Book("The fundamentals of Management", "Michael Scott");
        blockchain.add(new Block(book2,blockchain.get(blockchain.size()-1).hash));
        System.out.println("Trying to Mine block 2... ");
        blockchain.get(1).mineBlock(difficulty);

        Book book3 = new Book("To Jupiter and back","An astronaut");
        blockchain.add(new Block(book3,blockchain.get(blockchain.size()-1).hash));
        System.out.println("Trying to Mine block 3... ");
        blockchain.get(2).mineBlock(difficulty);

        System.out.println("\nBlockchain is Valid: " + isChainValid());

        String blockchainJson = new GsonBuilder().setPrettyPrinting().create().toJson(blockchain);
        System.out.println("\nThe block chain: ");
        System.out.println(blockchainJson);
    }

    //checks the validity of the blockchain
    public static boolean isChainValid(){
        Block currentBlock;
        Block previousBlock;
        String hashTarget = new String(new char[difficulty]).replace('\0', '0');


        for(int i=1; i < blockchain.size(); i++) {
            currentBlock = blockchain.get(i);
            previousBlock = blockchain.get(i-1);

            if(!currentBlock.hash.equals(currentBlock.calculateHash())){
                System.out.println("Current hashes are not equal");
                return false;
            }

            if(!previousBlock.hash.equals(currentBlock.previousHash)){
                System.out.println("Previous hashes not equal");
                return false;
            }

            if(!currentBlock.hash.substring( 0, difficulty).equals(hashTarget)) {
                System.out.println("This block hasn't been mined");
                return false;
            }

        }
        return true;

    }



}
