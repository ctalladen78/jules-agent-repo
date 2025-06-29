    if session:
        user = auth.get_user()
        st.write(f"Welcome, {user['email']}!")

        todos = todo_manager.get_todos()
        if todos:
            st.table(todos)
            # ... (Delete todo code remains unchanged) ...
        else:
            st.write("No todos found.") #Corrected this line

        # Add todo form -  Now uses React component for input
        st.components.v1.html(
            """
            <div id="root"></div>
            <script src="/static/build/static/js/main.js"></script>
            """,
            height=150,
        )


        # Handle todo addition from React component
        if st.request.method == 'POST':
            data = st.request.json()
            if data and 'prompt' in data:
                new_todo = data['prompt']
                token_count = count_tokens(new_todo) # Placeholder - Replace with actual token counting

                if token_count <= MAX_TOKENS:
                    result = todo_manager.add_todo(new_todo)
                    if result:
                        st.success("Todo added successfully!")
                        st.experimental_rerun()
                    else:
                        st.error("Error adding todo.")
                else:
                    st.error(f"Todo exceeds token limit ({MAX_TOKENS} tokens).")

    else:
        st.warning("Please sign in to access your to-do list.")

