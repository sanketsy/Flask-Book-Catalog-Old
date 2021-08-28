from app.catalog import main
from app.catalog.models import Book, Publication
from flask import render_template, url_for, flash, request, redirect
from flask_login import login_required
from app import db
from app.catalog.forms import EditBookForm, CreateBookForm

@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publishers_books = Book.query.filter_by(pub_id=publisher_id).all()
    return render_template('publisher.html', publisher=publisher, publishers_books=publishers_books)


@main.route('/delete/book/<book_id>', methods=['GET', 'POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get(book_id)

    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        flash('Book successfully deleted.')
        return redirect(url_for('main.display_books'))

    return render_template('delete_book.html', book=book, book_id=book_id)

@main.route('/edit/book/<book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    book = Book.query.get(book_id)
    editBookForm = EditBookForm(obj=book)

    if editBookForm.validate_on_submit():
        book.title = editBookForm.title.data
        book.format = editBookForm.format.data
        book.num_pages = editBookForm.num_pages.data
        db.session.add(book)
        db.session.commit()
        flash("Book details updated successfully!")
        return redirect(url_for('main.display_books'))

    return render_template("edit_book.html", editBookForm=editBookForm, book_id=book_id)

@main.route("/create/book/<pub_id>", methods=['GET', 'POST'])
@login_required
def create_book(pub_id):
    createBookForm = CreateBookForm()
    createBookForm.pub_id.data = pub_id  # To populate the pub_id textbox in the Form

    if createBookForm.validate_on_submit():
        book = Book(createBookForm.title.data,
                    createBookForm.author.data,
                    createBookForm.avg_rating.data,
                    createBookForm.format.data,
                    createBookForm.image.data,
                    createBookForm.num_page.data,
                    createBookForm.pub_id.data)
        db.session.add(book)
        db.session.commit()
        flash("Book added successfully..!")
        return redirect(url_for('main.display_publisher', publisher_id=pub_id))

    return render_template('create_book.html', createBookForm=createBookForm, pub_id=pub_id)


