import dnbinaryformat

from fixtures import *


def test_subtee_dntojscript(dntojscript):
    record_types = []
    for (_, record) in dnbinaryformat.deserialize(dntojscript):
        record_types.append(type(record))

    assert record_types == [
        dnbinaryformat.SerializationHeaderRecord,
        dnbinaryformat.SystemClassWithMembersAndTypes,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
        dnbinaryformat.SystemClassWithMembersAndTypes,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.MemberReference,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.ObjectNull,
        dnbinaryformat.SystemClassWithMembersAndTypes,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
        dnbinaryformat.SystemClassWithMembersAndTypes,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.MemberPrimitiveTyped,
          dnbinaryformat.ObjectNull,
        dnbinaryformat.ClassWithId,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.MemberReference,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.ObjectNull,
          dnbinaryformat.ArraySinglePrimitive,
        dnbinaryformat.ClassWithId,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
          dnbinaryformat.MemberReference,
          dnbinaryformat.BinaryObjectString,
          dnbinaryformat.MemberPrimitiveTyped,
          dnbinaryformat.ObjectNull,
        dnbinaryformat.MessageEnd,
    ]
