# Task: Implementing agentic LLM based Todo App with Supabase Authentication in Python and Streamlit

This README outlines the steps to build a Todo app with Supabase user authentication, the todo items are shown in streamlit dashboard 
the streamlit dashboard has login input for email and password

1. **Set up Supabase:** Configure your Supabase project and obtain your Supabase URL and anonymous key.  Create a `.env.local` file at the root of your project and add the following:

   ```
   NEXT_PUBLIC_SUPABASE_URL=<your_supabase_url>
   NEXT_PUBLIC_SUPABASE_ANON_KEY=<your_supabase_anon_key>
   ```

5. **Implement user authentication:**  Implement the authentication logic within the `Login` component using `@supabase/supabase-js`.

6. **Connect to Supabase:**  Connect both the `Todo` and `Login` components to your Supabase client.

7. **Implement server-side logic (optional):** If you need server-side rendering or data fetching, use `getServerSideProps` within your page components (e.g., `app/page.tsx`).

8. **Create API routes (optional):**  Use the `app/api` directory to create serverless API routes if needed.


