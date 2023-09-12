1. Exported Variables:
   - `sigilData`: This variable will be used to store the generated sigil data. It will be shared between `sigil_generator.js`, `views.py`, and `sigil.html`.

2. Data Schemas:
   - `Sigil`: This schema will be defined in `models.py` and will be used in `views.py` and `sigil_generator.js`. It will contain fields like `message`, `sigilCode`, and `sigilImage`.

3. ID Names of DOM Elements:
   - `sigilCanvas`: This is the id of the canvas element where the sigil will be rendered. It will be used in `sigil.html` and `sigil_generator.js`.
   - `messageInput`: This is the id of the input field where the user will enter the message or word. It will be used in `index.html` and `sigil_generator.js`.
   - `generateButton`: This is the id of the button that will trigger the sigil generation. It will be used in `index.html` and `sigil_generator.js`.

4. Message Names:
   - `generateSigil`: This message will be sent from `sigil_generator.js` to `views.py` to trigger the sigil generation.
   - `sigilGenerated`: This message will be sent from `views.py` to `sigil_generator.js` when the sigil has been generated.

5. Function Names:
   - `generateSigil()`: This function will be defined in `sigil_generator.js` and will be responsible for generating the sigil.
   - `renderSigil()`: This function will be defined in `sigil_generator.js` and will be responsible for rendering the sigil on the canvas.
   - `getSigilData()`: This function will be defined in `views.py` and will be responsible for retrieving the sigil data from the database.
   - `saveSigilData()`: This function will be defined in `views.py` and will be responsible for saving the sigil data to the database.