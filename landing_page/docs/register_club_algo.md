# Registration Form for Clubs — Algorithm

## Club Registration Function

### 1. Check Login Status
- Call `check_login_status()`
  - **If user is logged in:**
    - Proceed to Step 2.
  - **Else:**
    - Display a login-required message (e.g., popup or alert).
    - Redirect to the registration page.

### 2. Check Request Method
- **If request method is `GET`:**
  - Create an **empty registration form** instance.
  - Add the form to the context.
  - Render the registration page with the context.
  - **End process.**
- **Else if request method is `POST`:**
  - Proceed to Step 3.

### 3. Process Form Submission
- Create a form instance using the submitted `POST` data.
- Validate the form:
  - **If the form is valid:**
    1. Save the form using `commit=False` to delay saving to the database.
    2. Assign the current logged-in user’s ID or instance to the appropriate field  
       _(e.g., `form.instance.student = request.user`)_
    3. Save the form to the database using `form.save()`.
  - **If the form is invalid:**
    - The form will retain errors to be displayed on the page.

### 4. Render the Response
- Add the form (valid or invalid) to the context.
- Render the registration page with the context, displaying success or error messages as needed.