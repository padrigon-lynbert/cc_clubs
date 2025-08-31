# Club Registration Flow — Algorithm

## 1. Check   in Status
- If the user is **not logged in**:
  - Display an error message: `"You must be logged in to access this page."`
  - Redirect to the home page

## 2. If Request Method is POST
1. Bind form data to `ClubRegistrationForm`
2. Check if the form is **valid**
3. If **valid**:
    - Normalize and check if the club name already exists in the `Club` table
      - If it exists:
        - Display an error message: `"This club is already registered."`
        - Redirect to the registration page
    - If it doesn't exist:
        - Save the form instance without committing (`commit=False`)
        - Retrieve the student ID from the session
        - Query the `Students` table to get the corresponding student object
        - Assign the student to the `submitted_by` field of the form
        - Save the form to the database
        - Display a success message: `"Successfully submitted a club registration form."`
        - Redirect to the registration page
4. If **invalid**:
    - Display an error message: `"Invalid form submission."`

## 3. If Request Method is GET
- Initialize an empty `ClubRegistrationForm`

## 4. Render the Template
- Pass the form to the context
- Render the `register_club.html` template with the form
