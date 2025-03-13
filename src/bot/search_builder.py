''' 
Idea here is to be able to build a series of descriptors for a specific element

For example

descriptor_bundle = create_search_bundle()

# The element will have the class "button-green"
descriptor_bundle.add(Param.class("button-green"))

# Will have parent that has the name "form-group"
parent_bundle = create_search_bundle()
parent_bundle.add(Param.name("form-group"))

# Add the parent description to this search
descriptor_bundle.add(Param.parent(parent_bundle, 1))
# The 1 is to indicate this is the first parent, 2 would be the grandparent, and so on. Could also theoretically nest parent search within parent search

# Will have 3 children
descriptor_bundle.add(Param.has_child_count(3))

result = descriptor_bund.search()


# Should work for the following hypothetical HTML:

<form name="form-group">
  <button class="button-green"> <- should return this here element
    <div>This</div>
    <div>is</div>
    <div>it!</div>
  </button>
  <button class="button-blue">
    Not this button!
  </button>
</form>


'''