from CouchbaseLite.Database import Database, DatabaseConfiguration, IndexConfiguration, FullTextIndexConfiguration
from CouchbaseLite.Document import Document, MutableDocument
from CouchbaseLite.Query import JSONQuery, N1QLLanguage, JSONLanguage
import json

#Clean up any old DB
Database.deleteFile("db", "./")

def canonicalJSON(str):
    obj = json.loads(str)
    return json.dumps(obj, sort_keys = True)

db = Database("db", DatabaseConfiguration("./"))

print ("db    = ", db)
print ("name  = ", db.name)
print ("config= ", db.config)
print ("path  = ", db.path)
print ("docs  = ", db.count)

assert(db.name == "db")
assert(db.path == "./db.cblite2/")
assert(db.count == 0)

def dbListener(docIDs):
    print ("######## DB changed!", docIDs)
dbListenerToken = db.addListener(dbListener)

with db:
    doc = db.getDocument("foo")
    assert(not doc)
    doc = db.getMutableDocument("foo")
    assert(not doc)
    doc = MutableDocument("foo")
    assert(doc.id == "foo")

    print ("doc  = ", doc)

    props = doc.properties
    print ("props=", props)
    assert(props == {})

    props["flavor"] = "cardamom"
    props["numbers"] = [1, 0, 3.125]
    doc["color"] = "green"
    print ("props=", props)

    db.saveDocument(doc)

    doc2 = db.getDocument("foo")
    assert(doc2.id == "foo")
    print ("doc2 = ", doc2)
    props2 = doc2.properties
    print ("props2=", props2)
    assert(props2 == props)
    assert(doc2["color"] == "green")

    assert(db.count == 1)

    doc = MutableDocument("bar")
    doc["color"] = "green"
    doc["flavor"] = "pumpkin spice"
    db["bar"] = doc # saves it

    assert(db.count == 2)

    doc = MutableDocument('nested_doc')
    doc['flat'] = 'flat'
    doc['empty_obj'] = {}
    doc['nested'] = {'nested': 'nested'}
    doc['empty_array'] = []
    doc['array'] = ['a']
    print("doc = ", canonicalJSON(doc.JSON))
    assert(canonicalJSON(doc.JSON) == """{"array": ["a"], "empty_array": [], "empty_obj": {}, "flat": "flat", "nested": {"nested": "nested"}}""")
    db.saveDocument(doc)

    read_doc = db.getMutableDocument('nested_doc')
    print("read_doc = ", canonicalJSON(read_doc.JSON))
    assert(canonicalJSON(read_doc.JSON) == """{"array": ["a"], "empty_array": [], "empty_obj": {}, "flat": "flat", "nested": {"nested": "nested"}}""")
    db.saveDocument(read_doc)

    update_doc = db.getMutableDocument('nested_doc')
    update_doc['a'] = 'b'
    update_doc['nested']['foo'] = 'bar'
    print("update_doc = ", canonicalJSON(update_doc.JSON))
    assert(canonicalJSON(update_doc.JSON) == """{"a": "b", "array": ["a"], "empty_array": [], "empty_obj": {}, "flat": "flat", "nested": {"foo": "bar", "nested": "nested"}}""")
    db.saveDocument(update_doc)