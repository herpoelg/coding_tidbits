package coffee.learning;

import jdk.jfr.Threshold;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class SuperHeroes {

    public static void main(String args[]) {

        Integer bucketSize = 250;
        Double loadFactor = 0.85d;
        Double thresholdValue = bucketSize * loadFactor;
        System.out.println("Threshold value = "+ thresholdValue); //once passed, bucket size will be doubled and rehashing will happen
        System.out.println("------------------------------------------------");

        Map<String, Integer> allSuperHeroes = new HashMap<String, Integer>(250, 0.8f);
        System.out.println(allSuperHeroes.isEmpty() ? "Currently no superheroes in the universe" : "All hope is back");

        allSuperHeroes.put("Muesliman", 110);
        allSuperHeroes.put("GranolaBastard", 20);
        allSuperHeroes.put("AppleSquizer", 300);
        allSuperHeroes.put("Carrotwoman", 335);
        allSuperHeroes.put("Hulk", 500);

        Set<Map.Entry<String, Integer>> allSuperHeroesSet = allSuperHeroes.entrySet();
        System.out.println("*-*-*-: Superheroes in the universe :-*-*-*");
        for (Map.Entry<String, Integer> heroEntry : allSuperHeroesSet) {
            System.out.println("Name : " + heroEntry.getKey() + " " + " Strenth : " + heroEntry.getValue());
        }
        System.out.println("------------------------------------------------");
        System.out.println("No of superheroes in allSuperheroes : " + allSuperHeroes.size());
        System.out.println("Muesliman's power : " + allSuperHeroes.get("Muesliman"));
        System.out.println("Delete Hulk, he's not a real superhero : " + allSuperHeroes.remove("Hulk"));

    }

}
