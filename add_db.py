from app import app, db, Equipment, Location

with app.app_context():
    new_eq1 = Equipment(name='SONY A7S III', description='Професійна повнокадрова камера з високою чутливістю до світла і можливістю запису відео в 4K роздільній здатності.',
                       image='media/demo/author-1.jpg')

    new_eq2 = Equipment(name='Canon Mark 4',
                       description='Флагманська цифрова дзеркальна камера з високою роздільною здатністю і передовими технологіями автофокусування.',
                       image='media/demo/author-2.jpg')

    new_eq3 = Equipment(name='Godox SL150',
                        description='Потужний студійний спалах з LED-освітленням для професійної фото- і відеозйомки.',
                        image='media/demo/author-3.jpg')
    #
    # new_eq4 = Equipment(name='Blackmagic Pocket 6k Pro',
    #                     description='Ахуенная камера',
    #                     image='media/demo/author-4.jpg')

    #Додавання обладнання до сесії
    db.session.add(new_eq1)
    db.session.add(new_eq2)
    db.session.add(new_eq3)
    # db.session.add(new_eq4)
    # Збереження змін
    db.session.commit()

    eq = Equipment.query.all()
    print(eq)

    new_l1 = Location(name='Темна Елеганція',
                        description='Ідеальне місце для створення містичних та елегантних знімків',
                        image='media/demo/interior-1.jpg')

    new_l2 = Location(name='Світла Грація',
                        description='Легкість та невагомість світлої локації підкреслять красу та емоції ваших фото',
                        image='media/demo/interior-2.jpg')

    new_l3 = Location(name='Емеральдовий Простір',
                        description='Зелені відтінки локації нагадують про чарівність емеральдів, створюючи атмосферу свіжості та відновлення',
                        image='media/demo/interior-3.jpg')

    new_l4 = Location(name='Сонячна Симфонія',
                      description='Приємне тепло сонця, що проникає через наші панорамні вікна, робить цю локацію неперевершеною',
                      image='media/demo/interior-4.jpg')

    # Додавання обладнання до сесії
    db.session.add(new_l1)
    db.session.add(new_l2)
    db.session.add(new_l3)
    db.session.add(new_l4)
    # Збереження змін
    db.session.commit()



    # user_to_delete = Equipment.query.get(4)  # `user_id` - це ID користувача, якого ви хочете видалити
    #
    # if user_to_delete:
    #     # Видалення користувача з бази даних
    #     db.session.delete(user_to_delete)
    #
    #     # Збереження змін
    #     db.session.commit()