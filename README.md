# sharebite-backend

## Implementation for Sharebite backend API part of the assessment.

**Technologies used:** Python, Django REST framework

**Django project name:** restaurant

**Django app name:** menu

## More details

- Section is connected to Item through a Foreign Key (FK) in Item table. (One-to-one relationship)
- Items and Modifiers have many-to-many relationship. So, Items will have an array of the modifiers that belong to the particular item, and vice versa.
- So, for mapping Items and Modifiers, user needs to go to the endpoint (say, ```http://127.0.0.1:8000/menu/mapping/add/<primary-key-of-modifier>``` ), and enter the Items in the following format:
```
{
  "items":[1,3]
}
```

### Endpoints

#### Menu
- View entire menu: http://127.0.0.1:8000/menu/

#### Sections
- View all Sections: http://127.0.0.1:8000/menu/sections
  - Add section: http://127.0.0.1:8000/menu/sections/add/<primary-key>
  - Update section: http://127.0.0.1:8000/menu/sections/update/<primary-key>
  - Delete section: http://127.0.0.1:8000/menu/sections/delete/<primary-key>

#### Items
- View all Items: http://127.0.0.1:8000/menu/items
  - Add item: http://127.0.0.1:8000/menu/items/add/<primary-key>
  - Update item: http://127.0.0.1:8000/menu/items/update/<primary-key>
  - Delete item: http://127.0.0.1:8000/menu/items/delete/<primary-key>

#### Modifiers
- View all Modifiers: http://127.0.0.1:8000/menu/modifiers
  - Add modifier: http://127.0.0.1:8000/menu/modifiers/add/<primary-key>
  - Update modifier: http://127.0.0.1:8000/menu/modifiers/update/<primary-key>
  - Delete modifier: http://127.0.0.1:8000/menu/modifiers/delete/<primary-key>
  
#### Mappings
- Add mapping: http://127.0.0.1:8000/menu/mapping/add/<primary-key>
- Update modifier: http://127.0.0.1:8000/menu/mapping/update/<primary-key>

Note: For mappings, primary key of Modifiers should be used.
