from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='Anderson', email='andy@gmail.com', password='secret')
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'andy@gmail.com'))

    assert result.id == 1
