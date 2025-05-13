## Extra Credit Project

### Team Members

* Saksham Mehta \[sm2683]
* Soma Parvathini \[svp98]
* Syona Bhandari \[sb2199]
* Rhemie Patiak \[rmp260]

### Contributions

The project was collaborated on by Soma, Syona, Saksham, and Rhemie. We all participated in meetings to fix and debug code, and each member contributed equally to design, implementation, and testing.

---

### How to Run

1. **Prerequisites:**

   * Access to Rutgers ILAB machines (with PostgreSQL configured for your NetID)
   * Required Python packages:

     ```bash
     pip install llama-cpp-python paramiko pandas psycopg2-binary
     ```
   * On macOS, for GPU acceleration install `llama-cpp-python` with Metal support:

     ```bash
     CMAKE_ARGS="-DLLAMA_METAL=on" pip install -U llama-cpp-python --no-cache-dir
     ```

2. **Setup:**

   1. Download the LLM model file (`Phi-3.5-mini-instruct-Q4_K_M.gguf`) from the link in `Project_2.txt` and place it in the same directory as `database_llm.py`, or update the `MODEL_PATH` variable in `database_llm.py`.
   2. Copy the `ilab_script.py` to your home directory on your ILAB account:

      ```bash
      scp ilab_script.py your_netid@ilab.cs.rutgers.edu:~/
      ```

      Ensure it has execute permissions if needed.
   3. Verify that your PostgreSQL database is populated on `postgres.cs.rutgers.edu` with the tables defined in `schema.sql`.

3. **Execution:**

   ```bash
   python3 database_llm.py
   ```

   1. Enter your ILAB NetID and SSH password when prompted.
   2. Enter your natural-language queries about the database.
   3. Type `exit` to quit the application.

---

### What We Found Challenging

* **Prompt Engineering:** Crafting clear, concise prompts so the LLM consistently generates valid SQL statements was iterative and required fine-tuning keywords, schema context, and example queries.
* **SSH Integration:** Handling SSH connections and remote script execution through Paramiko introduced subtle issues around authentication timeouts and error handling in different network environments.
* **Result Parsing:** Extracting the SQL from the LLM’s raw output with a robust regex and then normalizing query results into a pandas DataFrame for JSON serialization demanded careful edge-case testing.
* **Schema Embedding:** Keeping the database schema in sync between the prompt, the `schema.sql` file, and the running database required strict version control to avoid mismatches.

### What We Found Interesting

* **LLM-to-SQL Translation:** Observing how the LLM maps diverse natural-language question formulations into precise SQL—often handling joins, filters, and aggregations correctly—was both surprising and insightful.
* **Interactive Workflow:** Building an end-to-end pipeline from query input through LLM reasoning to live database results provided a tangible demonstration of AI-assisted data exploration.
* **Error Recovery:** Seeing how small prompt tweaks could recover from malformed SQL outputs highlighted the power and flexibility of prompt-based programming.
* **Extensibility:** The modular design makes it straightforward to swap in different LLM backends or adapt the UI for additional features like query history, pagination, or visualization overlays.
