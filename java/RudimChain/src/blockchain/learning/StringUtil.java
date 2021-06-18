package blockchain.learning;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

//helper class
public class StringUtil {
    public static String applySha256(String input){
        try{

            MessageDigest digest = MessageDigest.getInstance("SHA-512");
            byte[] hash = digest.digest(input.getBytes("UTF-8"));

            // Convert byte array into signum representation
            BigInteger no = new BigInteger(1, hash);

            // Convert message digest into hex value
            String hashtext = no.toString(16);

            //ensuring a leading
           while (hashtext.length() < 128) {
                hashtext = "0" + hashtext;
            }

            // return the HashText
            return hashtext;

            //alternative with StringBuffer
            /*
            StringBuffer hexString = new StringBuffer();
            for(int i = 0; i < hash.length; i++){
                String hex = Integer.toHexString(0xff & hash[i]);
                if(hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }

            String strHexString;
            strHexString = hexString.toString();
            return strHexString;
            */

             
        }
        catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }

        catch (Exception e){
            throw new RuntimeException(e);
        }
    }
}
