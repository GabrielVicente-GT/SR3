import Obj
import gl

def crear():

    scale_factor = (12,12)
    translate_factor = (500, 50)

    cube = Obj.Obj('Bigmax_White_OBJ.obj')

    for face in cube.faces:
        if len(face) == 4:
            f1 = face[0][0] - 1
            f2 = face[1][0] - 1
            f3 = face[2][0] - 1
            f4 = face[3][0] - 1

            # print("cara", face)
            # print("vertices", cube.vertices)
            # print("f1", f1)
            # print("cubo", cube.vertices[f1])

            v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor)
            v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor)
            v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor)
            v4 = transform_vertex(cube.vertices[f4], scale_factor, translate_factor)

            gl.glLine2(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            gl.glLine2(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            gl.glLine2(v3[0][0], v3[0][1], v4[0][0],v4[0][1])
            gl.glLine2(v4[0][0], v4[0][1], v1[0][0],v1[0][1])



        elif len(face) == 3:
            f1 = face[0][0] - 1
            f2 = face[1][0] - 1
            f3 = face[2][0] - 1

            v1 = transform_vertex(cube.vertices[f1], scale_factor, translate_factor)
            v2 = transform_vertex(cube.vertices[f2], scale_factor, translate_factor)
            v3 = transform_vertex(cube.vertices[f3], scale_factor, translate_factor)

            gl.glLine2(v1[0][0], v1[0][1], v2[0][0],v2[0][1])
            gl.glLine2(v2[0][0], v2[0][1], v3[0][0],v3[0][1])
            gl.glLine2(v3[0][0], v3[0][1], v1[0][0],v1[0][1])


def transform_vertex(vertex, scale, translate):

    return [
        (
            (vertex[0] * scale[0]) + translate[0], #X.
            (vertex[1] * scale[1]) + translate[1] #Y.
        )
    ]


