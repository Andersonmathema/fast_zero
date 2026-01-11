from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        user = User(
            username='Anderson', email='andy@gmail.com', password='secret'
        )
        session.add(user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'Anderson'))

        assert asdict(user) == {
            'id': 1,
            'username': 'Anderson',
            'email': 'andy@gmail.com',
            'password': 'secret',
            'created_at': time,
        }
