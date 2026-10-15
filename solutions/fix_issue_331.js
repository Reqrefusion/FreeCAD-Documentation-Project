// Solution for issue #331
// Generated automatically by Baobot

To address the issue of external add-on documentation in the FreeCAD project, I need more specific details about the problem you're trying to solve. However, a common issue in documentation projects is ensuring that external add-ons are correctly referenced and described in the documentation. Below is a basic example of how you might create a script that attempts to fetch and reference external add-ons in the documentation, assuming the structure of the documentation is managed as a JSON file.

This example assumes that the documentation is structured as a JSON file where each add-on is described and its URL is provided.


const fetch = require('node-fetch');
const fs = require('fs');
const path = require('path');

// Sample structure for the JSON file
const documentationJsonPath = path.join(__dirname, 'documentation.json');
const externalDocsJsonPath = path.join(__dirname, 'externalDocs.json');

// Load the documentation
let docs;
try {
  docs = JSON.parse(fs.readFileSync(documentationJsonPath, 'utf8'));
} catch (error) {
  console.error('Error loading documentation:', error);
  process.exit(1);
}

// Load external add-on documentation
let externalDocs;
try {
  externalDocs = JSON.parse(fs.readFileSync(externalDocsJsonPath, 'utf8'));
} catch (error) {
  console.error('Error loading external documentation:', error);
  process.exit(1);
}

function updateDocumentation() {
  docs.addons.forEach(addon => {
    const addonUrl = externalDocs[addon.id];
    if (addonUrl) {
      addon.externalLink = `External Documentation: <a href="${addonUrl}">${addonUrl}</a>`;
    }
  });
}

updateDocumentation();

// Write the updated JSON back to file
fs.writeFileSync(documentationJsonPath, JSON.stringify(docs, null, 2), 'utf8');

console.log('Documentation updated with external links.');


To run this script, you would need to have the `node-fetch` package installed. You can install it using npm:

bash
npm install node-fetch


Then you can run the script:

bash
node updateDocumentation.js


Please adjust the paths (`documentationJsonPath`, `externalDocsJsonPath`) and the structure of the JSON files according to your actual project setup. Additionally, ensure that the `externalDocs` JSON file contains the correct URLs for the external add-ons.