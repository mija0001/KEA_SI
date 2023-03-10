import {Router } from "express"
const router = Router()

const toMetersDict = {    // Dictionary of units and their conversion to meters
    mm: 0.001,          // millimeter
    cm: 0.01,           // centimeter
    m: 1,               // meter
    km: 1000,           // kilometer
    mi: 1609.34,        // mile
    ft: 0.3048,         // foot
    yd: 0.9144,         // yard
    in: 0.0254,         // inch
    nmi: 1852,          // nautical mile
  };

const fromMetersDict = {  // Dictionary of units and their conversion from meters
    mm: 1000,           // millimeter
    cm: 100,            // centimeter
    m: 1,               // meter
    km: 0.001,          // kilometer
    mi: 0.000621371,    // mile
    ft: 3.28084,        // foot
    yd: 1.09361,        // yard
    in: 39.3701,        // inch
    nmi: 0.000539957,   // nautical mile
  };

/**
 * @openapi
 * /api/convert:
 *  post:
 *    summary: Convert from one unit of length to another
 *    requestBody:
 *      required: true
 *      content:
 *        application/json:
 *          schema:
 *            type: object
 *            properties:
 *              from:
 *                type: string
 *                description: The unit to convert from
 *                enum: [mm, cm, m, km, mi, ft, yd, in, nmi]
 *              to:
 *                type: string
 *                description: The unit to convert to
 *                enum: [mm, cm, m, km, mi, ft, yd, in, nmi]
 *              amount:
 *                type: number
 *                description: The amount to convert
 *    responses:
 *      200:
 *        description: The result of the conversion
 *        content:
 *          application/json:
 *            schema:
 *            type: object
 *            properties:
 *              result:
 *                type: number
 *      400:
 *        description: The request was invalid (e.g. missing parameters, invalid units, etc.)
 */
router.post("/api/convert", (req, res) => {
    const { from, to, amount } = req.body // Get from, to and amount from request body
    const result = convert(from, to, amount) // Call convert function with from, to and amount
    if (!isNaN(result)) { // If result is a number, return it.
        res.send({ result })
    } 
    else { // If result is an error message, set status code to 400, and return error message.
        res.status(400).send({ error: result })
    }
})

// Function to convert from one unit of length to another
function convert(from, to, amount) {
    // If amount is a number and units are recognized, convert and return result.
    if (!isNaN(amount) && from in toMetersDict && to in fromMetersDict) {
        return Number(amount) * toMetersDict[from] * fromMetersDict[to]
    }
    // If amount or units are not recognized, return error message.
    else {
        return "Invalid amount or unit"
    }
}

export default router