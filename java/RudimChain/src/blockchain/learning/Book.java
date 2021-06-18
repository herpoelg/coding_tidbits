package blockchain.learning;

//simple book class to represent the content of a block
public class Book {

    public String title;
    public String author;

    public Book(String title, String author){
        this.title = title;
        this.author = author;
    }

    @Override public String toString() {
        return "Title='" + this.title + "', Author=" + this.author;
    }

}
