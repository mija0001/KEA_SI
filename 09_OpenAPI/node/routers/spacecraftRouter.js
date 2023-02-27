import { Router } from "express";
const router = Router();

const spacecrafts = [{id: 1, name: "Apollo 11"}, 
                     {id: 2, name: "Apollo 12"}, 
                     {id: 3, name: "Apollo 13"}];

/**
 * @openapi
 * /api/spacecrafts/{spacecraftId}:
 *  parameters:
 *  - name: spacecraftId
 *    description: The unique identifier of the spacecraft
 *    in: path
 *    required: true
 *   
 *  get:
 *    summary: Get a spacecraft by id
 *    responses:
 *      200:
 *        description: The spacecraft corresponding to the provided `spacecraftId`
 *        content:
 *          application/json:
 *      404:
 *        description: The spacecraft corresponding to the provided `spacecraftId` was not found
 *        content:
 *          application/json:
 */

router.get("/api/spacecrafts/:spacecraftId", (req, res) => {
    const spacecraftId = parseInt(req.params.spacecraftId);
    const spacecraft = spacecrafts.find((spacecraft) => spacecraft.id == spacecraftId);
    if (spacecraft) {
        res.send({ data: spacecraft });
    } else {
        res.status(404).send({ error: "Spacecraft not found" });
    }
});

export default router;