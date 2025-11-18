# syntax=docker/dockerfile:1
FROM varnish:7.6

LABEL maintainer="Jorge Calasans <gabrielcalasaans@gmail.com>" \
      org.label-schema.name="tredf-varnish" \
      org.label-schema.description="Treinamento TRE-DF Varnish image." \
      org.label-schema.vendor="Jorge Calasans"

COPY etc/varnish.vcl /etc/varnish/default.vcl
