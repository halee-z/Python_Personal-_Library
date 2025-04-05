import streamlit as st
import pandas as pd

# Updated books list with all Harry Potter books and 3 parts of Doraemon
books = [
    {"Title": "Harry Potter and the Sorcerer's Stone", "Author": "J.K. Rowling", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "Harry Potter and the Chamber of Secrets", "Author": "J.K. Rowling", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "Harry Potter and the Prisoner of Azkaban", "Author": "J.K. Rowling", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "Harry Potter and the Goblet of Fire", "Author": "J.K. Rowling", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "Harry Potter and the Order of the Phoenix", "Author": "J.K. Rowling", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "Harry Potter and the Half-Blood Prince", "Author": "J.K. Rowling", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "Harry Potter and the Deathly Hallows", "Author": "J.K. Rowling", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "All of Us Are Dead", "Author": "Joo Dong-geun", "Genre": "Horror", "Status": "Unread"},
    {"Title": "Twilight", "Author": "Stephenie Meyer", "Genre": "Romance", "Status": "Unread"},
    {"Title": "Fate: The Winx Saga", "Author": "Brian Young", "Genre": "Fantasy", "Status": "Unread"},
    {"Title": "Doraemon: Part 1", "Author": "Fujiko F. Fujio", "Genre": "Sci-Fi", "Status": "Unread"},
    {"Title": "Doraemon: Part 2", "Author": "Fujiko F. Fujio", "Genre": "Sci-Fi", "Status": "Unread"},
    {"Title": "Doraemon: Part 3", "Author": "Fujiko F. Fujio", "Genre": "Sci-Fi", "Status": "Unread"},
]

df = pd.DataFrame(books)

st.title("📚 Haleema's Personal Library")

# --- Search ---
search = st.text_input("🔍 Search by title or author")
if search:
    filtered_df = df[df["Title"].str.contains(search, case=False) | df["Author"].str.contains(search, case=False)]
    st.dataframe(filtered_df)
else:
    st.dataframe(df)

# --- Filter by Status ---
st.subheader("🎯 Filter by Read/Unread")
status_filter = st.selectbox("Choose status", ["All", "Read", "Unread"])
if status_filter != "All":
    filtered = df[df["Status"] == status_filter]
    st.dataframe(filtered)

# --- Update Status ---
st.subheader("✅ Mark a Book as Read/Unread")
book_titles = df["Title"].tolist()
selected_book = st.selectbox("Select a book", book_titles)
new_status = st.selectbox("New Status", ["Read", "Unread"])

if st.button("Update Status"):
    df.loc[df["Title"] == selected_book, "Status"] = new_status
    st.success(f"📘 Status updated for '{selected_book}' to '{new_status}'")
    st.dataframe(df)
