from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(user_name='Anderson', email='and@gmail.com', password='senha')
    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'and@gmail.com'))

    assert result.user_name == 'Anderson'
