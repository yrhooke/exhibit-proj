# Exhibit

Artwork management tool

## TODO

- [X] use bootstrap with list and other detail views
- [X] add search navigation
- [ ] add image upload in update + create views (use whitenoise)
- [ ] make all list views into search views
- [ ] add some more css
- [ ] let user add artwork to an exhibition
- [ ] require user login
- [ ] allow search by foreignkey

### Further down goals

- [ ] dockerize or otherwise consider deployment
- [ ] add test suite


How I want search to work:

- you pick an model type. Then you get a list of potential fields (should be defined as public fields from within model) - this list remains constant if you don't switch model btw
- get a field selector and text box. if you select a foreignkey, a selector appears between first selector and text box- new selector contains that foreignkey's public field
- As soon as you enter some value, you get an and button that activates. pressing it opens another selector of the first type
- when you enter a query and press submit, it does a list view of search results (paginated), by anding the model.objects.
- at this point can't do OR and can't start over, but maybe tolerate having null values in some search fields


create view for search bar contents:
takes get params, returns the contents of the search bar
params fill the conetns of search bar - select the correct type, add a search field for eah field specified
returns xml

