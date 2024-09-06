#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const movieId = process.argv[2];

if (!movieId) {
    console.log("Usage: node starWarsCharacters.js <Movie ID>");
    process.exit(1);
}

async function getStarWarsCharacters(movieId) {
    try {
        // Fetch the film details from the Star Wars API
        const filmResponse = await fetch(`https://swapi.dev/api/films/${movieId}/`);
        if (!filmResponse.ok) {
            throw new Error(`Error fetching film data: ${filmResponse.statusText}`);
        }

        const filmData = await filmResponse.json();

        // Extract the characters list
        const characters = filmData.characters;

        // Print each character's name
        for (const characterUrl of characters) {
            const characterResponse = await fetch(characterUrl);
            if (!characterResponse.ok) {
                throw new Error(`Error fetching character data: ${characterResponse.statusText}`);
            }

            const characterData = await characterResponse.json();
            console.log(characterData.name);
        }

    } catch (error) {
        console.error(error.message);
    }
}

getStarWarsCharacters(movieId);