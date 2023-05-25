import redis from "redis";

const redisClient = redis.createClient();

redisClient.on("error", (error) => {
    console.error("Error", error);
});

redisClient.on("connect", () => console.log("Connected to Redis"));

await redisClient.connect();

redisClient.set("myKey", "some value");
const value = await redisClient.get("myKey");
console.log(value);

// redisClient.setEx("myKey", 10, "some value");