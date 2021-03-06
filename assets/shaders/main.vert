#version 130
in vec4 p3d_Vertex;
in vec3 p3d_Normal;
in vec2 p3d_MultiTexCoord0;
out vec3 pos;
out vec3 normal;
out vec2 texcoord;
out vec4 shadowcoord;
out vec4 lightclip;
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelViewMatrix;
uniform mat3 p3d_NormalMatrix;
uniform vec4 mspos_light;
uniform mat4 trans_model_to_clip_of_light;

float saturate(float v) { return clamp(v, .0, 1.0); }

void main() {
    texcoord = p3d_MultiTexCoord0;
    vec4 pushed = p3d_Vertex + vec4(p3d_Normal * .8, 0);
    lightclip = trans_model_to_clip_of_light * pushed;
    shadowcoord = lightclip * vec4(.5, .5, .5, 1) +
                  lightclip.w * vec4(.5, .5, .5, 0);
    normal = normalize(p3d_NormalMatrix * p3d_Normal);
    pos = vec3(p3d_ModelViewMatrix * p3d_Vertex);
    gl_Position = p3d_ModelViewProjectionMatrix  * p3d_Vertex;
}