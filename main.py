import os
import UnityPy


def unpack_all_assets(source_folder: str, destination_folder: str):
    env = UnityPy.load("movie_card_00512")

    # iterate over internal objects
    for assets in env.objects:
        data = assets.read()
        print(data)
        if data.type.name == "Sprite":
            data =data.read()
            path = os.path.join( f"{data.m_Name}.png")
            data.image.save(path)

        # for object in assets.objects:
        #     print(object)
        #     # process specific object types
        #     if obj.type.name in ["Texture2D", "Sprite"]:
        #         # parse the object data
        #         data = obj.read()

        #         # create destination path
        #         dest = os.path.join(destination_folder, data.name)

        #         # make sure that the extension is correct
        #         # you probably only want to do so with images/textures
        #         dest, ext = os.path.splitext(dest)
        #         dest = dest + ".png"

        #         img = data.image
        #         img.save(dest)


unpack_all_assets(".", ".")
