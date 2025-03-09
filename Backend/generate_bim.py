import ifcopenshell

def create_ifc_model(filename="model.ifc"):
    # Create a new IFC file
    model = ifcopenshell.file()

    # You need to create a basic IFC project setup. Without this,
    # many IFC viewers won't be able to open the file.

    # Create an IfcProject (required)
    project = model.create_entity("IfcProject", ifcopenshell.guid.new(), "My Project")

    # Create an IfcSite and IfcBuilding (also often required)
    site = model.create_entity("IfcSite", ifcopenshell.guid.new(), "My Site")
    building = model.create_entity("IfcBuilding", ifcopenshell.guid.new(), "My Building")

    # Create a wall (example) - create the basic entity *without* trying to set properties that don't exist
    wall = model.create_entity("IfcWall", ifcopenshell.guid.new())

    #Save the IFC file
    model.write(filename)
    print(f"BIM Model Generated: {filename}")

if __name__ == "__main__":
    create_ifc_model()