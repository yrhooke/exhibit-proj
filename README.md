# Exhibit

Artwork management tool

## TODO

- [ ] use bootstrap with list and other detail views
- [ ] add search navigation
- [ ] add image in update + create views (use whitenoise)
- [ ] add some css
- [ ] let user add artwork to an exhibition
- [ ] add image in list views

### Further down goals

- [ ] require user login
- [ ] dockerize or otherwise consider deployment


How I want search to work:

- you pick an model type. Then you get a list of potential fields (should be defined as public fields from within model) - this list remains constant if you don't switch model btw
- get a field selector and text box. if you select a foreignkey, a selector appears between first selector and text box- new selector contains that foreignkey's public field
- As soon as you enter some value, you get an and button that activates. pressing it opens another selector of the first type
- when you enter a query and press submit, it does a list view of search results (paginated), by anding the model.objects.
- at this point can't do OR and can't start over, but maybe tolerate having null values in some search fields
  