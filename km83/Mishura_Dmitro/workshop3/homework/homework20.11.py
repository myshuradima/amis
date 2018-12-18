def market_list(sn, arr=[], n=0):
    """
    Рекурсивна функція, яка повертає список всіх магазинів
    :param sn:
    :param arr:
    :param n:
    :return:
    """
    key = list(sn.keys())
    if (n == len(key)):
        print(set(arr))
        return
    else:
        arr = arr + list(sn[key[n]]["supermarkets"].keys())
        market_list(sn, arr, n + 1)


def prod_place(sn, nm):
    """
    Фукнкція, яка повертає список магазинів, в яких продається певна річ
    :param sn:
    :param nm:
    :return:
    """
    arr = []
    for elem in sn.values():
        for mag in elem["supermarkets"]:
            for prod in elem["supermarkets"][mag]:
                for elemen in prod.values():
                    if (elemen["name"] == nm):
                        arr.append(mag)
    return (set(arr))

dataset = {
    "smth": {
        "client": {
            "name": "bob",
            "surname": "bobenko",
            "age": 35
        },
        "supermarkets": {"fora": [
            {
                "prod1": {
                    "price": 10,
                    "name": "paper"
                }
            },
            {
                "prod2": {
                    "price": 15,
                    "name": "pen",
                }
            }
        ],

            "atb": [{
                "prod1": {
                    "price": 8,
                    "name": "paper"
                }
            }
            ],
            "novus": [{
                "prod2": {
                    "price": 15,
                    "name": "pen"
                }
            }
            ]

        }},
    "smth2": {
        "client": {
            "name": "boba",
            "surname": "familiya",
            "age": 40
        },
        "supermarkets": {"fora": [{"prod1": {
            "price": 20,
            "name": "knife"
        }},
            {"prod2": {
                "price": 15,
                "name": "pen"
            }}
        ],
            "atb": [{"prod1": {
                "price": 80,
                "name": "phone"
            }}
            ],
            "silpo": [{"prod1": {
                "price": 75,
                "name": "paper"
            }}]

        }
    }
}



market_list(dataset)
print(prod_place(dataset, "paper"))