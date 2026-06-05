# Problem: Create a simple “contact manager” that saves contacts to a JSON file (load, add, save).
## Solution: 
- In main.py

# Developer Notes: JSON Contact Manager

## 📂 Project Overview
A lightweight, Command Line Interface (CLI) application that performs **CRUD** (Create, Read) operations on a localized text database using Python's built-in modules.

---

## 🛠️ System Architecture & Workflow

1. **Initialization:** The program boots up and calls `load_contacts()`.
2. **Runtime Memory:** Active data is processed inside volatile memory as a standard Python **list of dictionaries**.
3. **Synchronization (Persistence):** Any data-altering event (like adding an entry) automatically calls `save_contacts()` to sync memory data onto the physical disk.

---

## 🔬 Deep Dive: Core Functions Analysis

### 1. Data Ingestion: `load_contacts()`
```python
def load_contacts():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
```
* **Defensive Design (`os.path.exists`)**: Prevents runtime crashes (`FileNotFoundError`) by providing a graceful fallback (empty list `[]`) if the file has not been created yet.
* **Type Parsing (`json.load`)**: Converts serialized JSON datatypes into matching functional runtime elements:
  * `[]` (JSON Array) \(\rightarrow\) `[]` (Python List)
  * `{}` (JSON Object) \(\rightarrow\) `{}` (Python Dictionary)
* **Exception Isolation**: Uses `try-except` to intercept structural corruptions (e.g., missing brackets, manual text editing mistakes) without killing the overall program execution.

### 2. Output Formatting: `list_contacts()`
```python
for index, contact in enumerate(contacts, 1):
    name = contact.get('name', 'N/A')
```
* **Index Alignment (`enumerate(..., 1)`)**: Overrides Python's base-0 counting indexing loop, making data lists instantly human-readable (starting from `1`).
* **Crash Safeguards (`.get()`)**: Accessing properties using standard bracket notations (`contact['email']`) risks throwing a terminal **`KeyError`** if the record is malformed. The `.get('key', default)` system safely returns a string fallback value (`'N/A'`) instead.

### 3. File System Sync: `save_contacts()`
```python
with open(FILENAME, "w") as file:
    json.dump(contacts, file, indent=4)
```
* **Context Management (`with open(...)`)**: Automatically shuts down and safely releases system read/write locks on files even if code execution encounters a sudden halt inside the scope block.
* **Overwriting Configuration (`"w"`)**: Empties out obsolete system string layouts inside the file entirely to write down a fresh snapshot of active runtime collections.
* **Pretty Printing (`indent=4`)**: Generates neat multi-line spacing inside the `.json` output file instead of a long single line of text, allowing humans to view data updates comfortably.

---

## ⚠️ Key Operational Diagnostics & Traps

### ⚡ Context Confusion (Terminal vs Script Locations)
Relative system execution strings like `open("contacts.json")` do not resolve path values relative to your source code's subdirectory position. They calculate paths from **where your command line window is opened**.

* **The Trap**: Running `python main.py` outside of the project subfolder creates fragmented `.json` files scattered in wrong directories, or triggers file path missing failures.
* **The Blueprint Fix**:
  ```python
  SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
  FILENAME = os.path.join(SCRIPT_DIR, "contacts.json")
  ```

---

## 🚀 Future Feature Roadmap Suggestions
To transform this into a professional production-grade application, the next logical implementations should be:
* **Data Deletion**: Add a menu entry that targets an array element by its index number (`contacts.pop(index - 1)`) to remove invalid listings.
* **Data Verification**: Use clean string filtering rules (like checking for an `@` symbol) to validate input strings before saving them to disk.
